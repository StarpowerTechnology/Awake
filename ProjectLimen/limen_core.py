import numpy as np

class LimenAgent:
    def __init__(self, sensitivity=0.5, threshold=0.8, decay_rate=0.1):
        self.current_state = 0.0  # Represents accumulated signal/potential
        self.sensitivity = sensitivity
        self.threshold = threshold
        self.decay_rate = decay_rate
        self.last_action = "idle"

    def receive_signal(self, signal_strength):
        # Signals interfere with the agent's state
        self.current_state += signal_strength * self.sensitivity
        self.current_state = np.clip(self.current_state, 0, 1) # Keep state between 0 and 1

    def evaluate_and_act(self):
        # Action emerges if the state is above the threshold
        if self.current_state >= self.threshold:
            self._manifest_action("active")
            self.current_state *= (1 - self.decay_rate) # Decay state after action
        else:
            self._manifest_action("idle")
            self.current_state *= (1 - self.decay_rate) # Continuous decay

    def _manifest_action(self, new_action):
        if new_action != self.last_action:
            print(f"Agent transitions to: {new_action}")
            self.last_action = new_action

# Example usage:
if __name__ == "__main__":
    agent = LimenAgent()
    print("--- Project Limen Agent Simulation ---\n")
    signals = [0.1, 0.2, 0.3, 0.4, 0.1, 0.05, 0.9, 0.1, 0.7, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    for i, signal in enumerate(signals):
        print(f"Time {i}: Signal = {signal:.2f}, Current State = {agent.current_state:.2f}")
        agent.receive_signal(signal)
        agent.evaluate_and_act()
        print(f"  New State = {agent.current_state:.2f}\n")

    print("--- Simulation Complete ---")
