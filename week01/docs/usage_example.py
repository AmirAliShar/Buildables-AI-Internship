
from utils.llm_helpers import Summarizer
from utils.Schema import InputState

def main():
    query = "What is the capital of Pakistan?"
    input_state = InputState(query=query)

    # Call your helper function
    response = Summarizer(input_state.query)
    print("Query:", input_state.query)
    print("Response:", response)

if __name__ == "__main__":
    main()
