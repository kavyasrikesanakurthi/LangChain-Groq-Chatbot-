from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)
db=[]
while True:
    msg=input("user:")
    db.append(("user",msg))
    if msg=="stop":
        break
    resp=llm.invoke(db)
    print(f"ai:{resp.content}")
    db.append("ai:,resp.content")