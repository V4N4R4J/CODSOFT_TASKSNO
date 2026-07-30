import re

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())

def get_response(user_input: str) -> str:
    text = normalize(user_input)

    if not text:
        return "I’m here! Ask me anything."

    if re.search(r"\b(hi|hello|hey|hola|good morning|good afternoon|good evening|greetings)\b", text):
        return "Hello! It’s nice to chat with you. How can I assist you today?"

    if re.search(r"\b(what is your name|who are you|what are you)\b", text):
        return "I’m an Simple rule-based chatbot designed to handle simple conversations and common questions."

    if re.search(r"\b(how are you|how do you do)\b", text):
        return "I’m doing great, thanks for asking! How are you doing today?"

    if re.search(r"\b(thank you|thanks|thank you so much)\b", text):
        return "You’re very welcome! I’m happy to help."

    if re.search(r"\b(help|what can you do|features)\b", text):
        return "I can greet you, answer simple questions, talk about weather or time, tell jokes, and keep a casual conversation going."

    if re.search(r"\b(weather|temperature|rain|sunny|cloudy|storm)\b", text):
        return "I can help with general weather-related conversation, but I can’t check live weather updates."

    if re.search(r"\b(time|date|today|day)\b", text):
        return "I can help with general time-related questions, although I don’t have a live clock."

    if re.search(r"\b(joke|tell me a joke|funny)\b", text):
        return "Sure! Why do programmers prefer dark mode? Because light attracts bugs."

    if re.search(r"\b(bye|goodbye|exit|quit|see you)\b", text):
        return "Goodbye! It was nice chatting with you."

    if re.search(r"\b(love|music|movie|game|sport|book|travel)\b", text):
        return "That sounds interesting! I’d be happy to talk about it with you."

    if text.endswith("?"):
        return "That’s a thoughtful question. I can help with greetings, small talk, weather, time, or jokes."

    return "I’m listening. Tell me more, or ask me something like help, weather, time, or a joke."


def main() -> None:
    print("Simple Rule-Based Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Bot: {response}")

        if normalize(user_input) in {"bye", "goodbye", "exit", "quit", "see you"}:
            break


if __name__ == "__main__":
    main()
