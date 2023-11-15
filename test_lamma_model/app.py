from langchain import PromptTemplate, LLMChain

from langchain.llms.ctransformers import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# llm = AutoModelForCausalLM.from_pretrained(
#     "TheBloke/CodeLlama-34B-Instruct-GGUF",
#     model_file="codellama-34b-instruct.Q5_K_M.gguf",
#     model_type="llama",
#     gpu_layers=0,
# )

# print(llm("AI is going to"))
config = {
    "max_new_tokens": 4096,
    "repetition_penalty": 1.1,
    "context_length": 4096,
}

llm = CTransformers(
    model="/home/ai/projects/ai-checker-code/test_lamma_model",
    model_file="phind-codellama-34b-v2.Q4_K_M.gguf",
    model_type="llama",
    config=config,
    callbacks=[StreamingStdOutCallbackHandler()],
)

response = llm("Create connection graphql with react and fastapi")

print(response)
# V2
# llm = AutoModelForCausalLM.from_pretrained(
#     "TheBloke/Phind-CodeLlama-34B-v2-GGUF",
#     model_file="phind-codellama-34b-v2.Q5_K_M.gguf",
#     model_type="llama",
#     gpu_layers=0,
# )

# print(llm("AI is going to"))


# llm = CTransformers(
#     model="TheBloke/Phind-CodeLlama-34B-v2-GGUF",
#     model_file="phind-codellama-34b-v2.Q5_K_M.gguf",
#     model_type="llama",
# )


# template = """
#               Write a concise summary of the following text delimited by triple backquotes.
#               Return your response in bullet points which covers the key points of the text.
#               ```{text}```
#               BULLET POINT SUMMARY:
#            """

# prompt = PromptTemplate(template=template, input_variables=["text"])

# llm_chain = LLMChain(prompt=prompt, llm=llm)

# text2 = """
# Apple Inc. is an American multinational technology company headquartered in Cupertino, California. Apple is the world's largest technology company by revenue, with US$394.3 billion in 2022 revenue.[6] As of March 2023, Apple is the world's biggest company by market capitalization.[7] As of June 2022, Apple is the fourth-largest personal computer vendor by unit sales and the second-largest mobile phone manufacturer in the world. It is often considered as one of the Big Five American information technology companies, alongside Alphabet (parent company of Google), Amazon, Meta Platforms, and Microsoft.

# Apple was founded as Apple Computer Company on April 1, 1976, by Steve Wozniak, Steve Jobs (1955–2011) and Ronald Wayne to develop and sell Wozniak's Apple I personal computer. It was incorporated by Jobs and Wozniak as Apple Computer, Inc. in 1977. The company's second computer, the Apple II, became a best seller and one of the first mass-produced microcomputers. Apple went public in 1980 to instant financial success. The company developed computers featuring innovative graphical user interfaces, including the 1984 original Macintosh, announced that year in a critically acclaimed advertisement called "1984". By 1985, the high cost of its products, and power struggles between executives, caused problems. Wozniak stepped back from Apple and pursued other ventures, while Jobs resigned and founded NeXT, taking some Apple employees with him.

# As the market for personal computers expanded and evolved throughout the 1990s, Apple lost considerable market share to the lower-priced duopoly of the Microsoft Windows operating system on Intel-powered PC clones (also known as "Wintel"). In 1997, weeks away from bankruptcy, the company bought NeXT to resolve Apple's unsuccessful operating system strategy and entice Jobs back to the company. Over the next decade, Jobs guided Apple back to profitability through a number of tactics including introducing the iMac, iPod, iPhone and iPad to critical acclaim, launching the "Think different" campaign and other memorable advertising campaigns, opening the Apple Store retail chain, and acquiring numerous companies to broaden the company's product portfolio. When Jobs resigned in 2011 for health reasons, and died two months later, he was succeeded as CEO by Tim Cook.

# Apple became the first publicly traded U.S. company to be valued at over $1 trillion in August 2018, then at $2 trillion in August 2020, and at $3 trillion in January 2022. As of April 2023, it was valued at around $2.6 trillion. The company receives criticism regarding the labor practices of its contractors, its environmental practices, and its business ethics, including anti-competitive practices and materials sourcing. Nevertheless, the company has a large following and enjoys a high level of brand loyalty. It has also been consistently ranked as one of the world's most valuable brands.
# """
# print(llm_chain.run(text2))
