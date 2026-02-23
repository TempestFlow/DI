"""
Water Jug Problem Solver using AIMA Search Architecture
Requires AIMA Python repository files: search.py and utils.py in the same directory.
"""

from search import Problem, breadth_first_graph_search


class WaterJugProblem(Problem):
    def __init__(self, initial=(0, 0), goal=2):
        """
        Initializes the problem.
        State is represented as a tuple: (jug4_amount, jug3_amount).
        Goal is defined as the target amount of water in the 4-gallon jug.
        """
        super().__init__(initial, goal)
        self.jug4_capacity = 4
        self.jug3_capacity = 3

    def actions(self, state):
        """
        Returns a list of valid actions for the current state.
        Filters out actions that would not result in a state change.
        """
        j4, j3 = state
        possible_actions = []

        # Fill actions
        if j4 < self.jug4_capacity:
            possible_actions.append('Fill Jug4')
        if j3 < self.jug3_capacity:
            possible_actions.append('Fill Jug3')

        # Empty actions
        if j4 > 0:
            possible_actions.append('Empty Jug4')
        if j3 > 0:
            possible_actions.append('Empty Jug3')

        # Pour actions
        if j4 > 0 and j3 < self.jug3_capacity:
            possible_actions.append('Pour Jug4 to Jug3')
        if j3 > 0 and j4 < self.jug4_capacity:
            possible_actions.append('Pour Jug3 to Jug4')

        return possible_actions

    def result(self, state, action):
        """
        Returns the new state resulting from applying the given action.
        """
        j4, j3 = state

        if action == 'Fill Jug4':
            return (self.jug4_capacity, j3)

        elif action == 'Fill Jug3':
            return (j4, self.jug3_capacity)

        elif action == 'Empty Jug4':
            return (0, j3)

        elif action == 'Empty Jug3':
            return (j4, 0)

        elif action == 'Pour Jug4 to Jug3':
            # Calculate how much water can actually be poured
            amount_to_pour = min(j4, self.jug3_capacity - j3)
            return (j4 - amount_to_pour, j3 + amount_to_pour)

        elif action == 'Pour Jug3 to Jug4':
            # Calculate how much water can actually be poured
            amount_to_pour = min(j3, self.jug4_capacity - j4)
            return (j4 + amount_to_pour, j3 - amount_to_pour)

        # Fallback (should not be reached if actions are correctly filtered)
        return state

    def goal_test(self, state):
        """
        Checks if the 4-liter jug has exactly the goal amount of water (2 liters).
        """
        return state[0] == self.goal


if __name__ == "__main__":
    # 1. Instantiate the problem
    water_jug_problem = WaterJugProblem(initial=(0, 0), goal=2)

    # 2. Solve using Breadth-First Graph Search to guarantee shortest path
    print("Searching for a solution...\n")
    goal_node = breadth_first_graph_search(water_jug_problem)

    # 3. Extract and format the results
    if goal_node:
        print("✅ Solution found!")
        path = goal_node.path()

        # Print table header
        print(f"{'Step':<5} | {'Action Applied':<20} | {'Current State (Jug4, Jug3)'}")
        print("-" * 60)

        # Print step-by-step trace
        for step, node in enumerate(path):
            action = node.action if node.action else "Initial State"
            state = node.state
            print(f"{step:<5} | {action:<20} | {state}")

        print(f"\nTotal steps required: {len(path) - 1}")
    else:
        print("❌ No solution could be found.")
