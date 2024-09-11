class Agent:
    def __init__(self, name):
        self.name = name

    def generate_response(self, message):
        return f"{self.name}: I hear you. You said '{message}', let me respond to that."

    def generate_conclusion(self):
        return f"{self.name}: After our discussion, I conclude that we have reached a mutual understanding."


def conversation(agent1, agent2, iterations=5):
    conversation_history = []
    message = "Initial message to start the conversation."

    for i in range(iterations):
        # Agent 1 responds
        response_a = agent1.generate_response(message)
        conversation_history.append(response_a)
        print(response_a)

        # Agent 2 responds
        response_b = agent2.generate_response(message)
        conversation_history.append(response_b)
        print(response_b)

        # Update the message for the next iteration
        message = response_b

    # Generate conclusions
    conclusion_a = agent1.generate_conclusion()
    conclusion_b = agent2.generate_conclusion()

    # Print conclusions
    print(conclusion_a)
    print(conclusion_b)

    # Add conclusions to history
    conversation_history.append(conclusion_a)
    conversation_history.append(conclusion_b)

    return conversation_history


# Initialize two agents
agent1 = Agent("FamousAgentA")
agent2 = Agent("FamousAgentB")

# Run the conversation for 5 iterations
conversation_history = conversation(agent1, agent2)

# Optionally, print the conversation history
print("\nFull conversation history:")
for entry in conversation_history:
    print(entry)
