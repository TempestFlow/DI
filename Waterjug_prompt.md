Act as an expert Python AI developer. I need you to write a complete, bug-free Python script that solves the "Water Jug Problem" using the AIMA (Artificial Intelligence: A Modern Approach) search architecture. 

Context: We have a 4-liter jug and a 3-liter jug. The goal is to measure exactly 2 liters of water in the 4-liter jug. 

Strict Requirements:
1. Assume the AIMA `search.py` and `utils.py` files are in the same directory. Import the `Problem` class and `breadth_first_graph_search` algorithm from `search`.
2. Create a class called `WaterJugProblem` that strictly inherits from AIMA's `Problem` class.
3. The state must be represented as a tuple: `(jug4_amount, jug3_amount)`. The initial state is `(0, 0)`.
4. Implement `__init__(self, initial=(0, 0), goal=2)`.
5. Implement the `actions(self, state)` method. The valid string actions are: 'Fill Jug4', 'Fill Jug3', 'Empty Jug4', 'Empty Jug3', 'Pour Jug4 to Jug3', 'Pour Jug3 to Jug4'. Only return actions that actually change the state.
6. Implement the `result(self, state, action)` method. It must return a new tuple `(new_jug4, new_jug3)` based on the applied action and the math of pouring water.
7. Implement the `goal_test(self, state)` method. It should return True if `state[0] == self.goal`.
8. At the bottom of the script, inside an `if __name__ == "__main__":` block, instantiate the `WaterJugProblem`.
9. Solve it using `breadth_first_graph_search`. 
10. Extract the sequence of actions and states from the resulting node's path and print them clearly to the console so I can see the step-by-step solution.

Do not use any external libraries other than the local AIMA files. The code must be ready to execute immediately without any human edits.
