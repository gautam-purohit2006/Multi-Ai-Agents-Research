"""
Flask UI for Multi-Ai-Agents-Research.

Does NOT modify or import pipline.py (it runs at import time with a fixed topic).
Instead it re-uses the same building blocks: agents.py and prompt_and_chain.py,
and runs the same 4-step flow for any topic typed in the UI.
"""
import json
from flask import Flask, render_template, request, Response

from agents import build_search_agent, build_reader_agents
from prompt_and_chain import writer_chain, critic_chain

app = Flask(__name__)


def sse(payload: dict) -> str:
    return f"data: {json.dumps(payload)}\n\n"


def as_text(result) -> str:
    """Chains may return str or a message object."""
    return result if isinstance(result, str) else getattr(result, "content", str(result))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run")
def run():
    topic = (request.args.get("topic") or "").strip()

    def stream():
        if not topic:
            yield sse({"type": "error", "message": "Please enter a topic."})
            return

        step = "search"
        try:
            # 1. Search agent
            yield sse({"type": "start", "step": step})
            search_out = build_search_agent().invoke({"messages": [("user", topic)]})
            search_text = search_out["messages"][-1].content
            yield sse({"type": "done", "step": step, "content": search_text})

            # 2. Reader agent
            step = "reader"
            yield sse({"type": "start", "step": step})
            reader_out = build_reader_agents().invoke({"messages": [("user", search_text)]})
            reader_text = reader_out["messages"][-1].content
            yield sse({"type": "done", "step": step, "content": reader_text})

            # 3. Writer chain
            step = "writer"
            yield sse({"type": "start", "step": step})
            writer_text = as_text(writer_chain.invoke({
                "topic": topic,
                "research_data": reader_text,
            }))
            yield sse({"type": "done", "step": step, "content": writer_text})

            # 4. Critic chain
            step = "critic"
            yield sse({"type": "start", "step": step})
            critic_text = as_text(critic_chain.invoke({"research_report": writer_text}))
            yield sse({"type": "done", "step": step, "content": critic_text})

            yield sse({"type": "complete"})
        except Exception as exc:  # surface errors in the UI
            yield sse({"type": "error", "step": step, "message": str(exc)})

    return Response(
        stream(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    app.run(debug=True, threaded=True, use_reloader=False, port=5000)