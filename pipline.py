from agents import  build_search_agent, build_reader_agents
from prompt_and_chain import writer_chain, critic_chain

data = {}
topic = "GPT-6 features, capabilities, and latest developments"

#First Agent
search_agent = build_search_agent()

search_agent_result = search_agent.invoke({
    "messages":[("user" ,topic)]
})

# print("= "*25)
# print("\n First Agent AI result \n")
# print("= "*25)

data['search_agent_result'] = search_agent_result["messages"][-1].content
# print(data['search_agent_result'])

#Second Agents
reader_agents = build_reader_agents()

reader_agents_result = reader_agents.invoke({
    "messages":[("user",data['search_agent_result'])]
})

# print("= "*25)
# print("\n Second Agent AI result \n")
# print("= "*25)

data["reader_agent_result"] = reader_agents_result["messages"][-1].content
# print(data["reader_agent_result"])


#Writer Chain

writer_chain_result = writer_chain.invoke({
        "topic" : topic,
        "research_data" : data["reader_agent_result"]
    })

data['writer_chain_result'] = writer_chain_result

# print(writer_chain_result)

#Critic Chain
critic_chain_result = critic_chain.invoke({
    "research_report": data['writer_chain_result']
})

data['critic_chain_result'] = critic_chain_result

print(data['critic_chain_result'])