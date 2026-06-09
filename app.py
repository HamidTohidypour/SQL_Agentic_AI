from graph import graph

while True:
    q = input("You: ")
    if q == "exit":
        break

    result = graph.invoke({"question": q})
    print("Bot:", result["result"])