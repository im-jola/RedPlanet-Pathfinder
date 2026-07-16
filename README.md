# RedPlanet-Pathfinder 🚀

An autonomous Mars Rover pathfinding simulator built in Python using Matplotlib and NumPy. The rover navigates a 10x10 grid, dynamically avoiding randomly generated boulder hazards and plotting the most efficient route to a science target zone using **Manhattan Distance** heuristics.

---

## 🧭 How It Works

The simulation sets up a coordinate grid representing the Martian surface:
* **Dark Blue (`0`):** Clear, traversable Martian ground.
* **Light Grey (`1`):** Randomly generated boulder obstacles that the rover must navigate around.
* **Deep Red (`2`):** The target science objective.
* **Coral / Light Peach (`1.5`):** The path traversed by the rover.

The rover uses a **Manhattan Distance** heuristic to evaluate adjacent legal moves at each step:
$$\text{Score} = |x_{\text{target}} - x_{\text{current}}| + |y_{\text{target}} - y_{\text{current}}|$$

It dynamically avoids obstacles, prevents backtracking, and stops animating the moment it reaches the target coordinates.

---

## 🛠️ Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/im-jola/RedPlanet-Pathfinder.git](https://github.com/im-jola/RedPlanet-Pathfinder.git)
   cd RedPlanet-Pathfinder
