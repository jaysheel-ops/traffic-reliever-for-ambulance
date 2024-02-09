import tkinter as tk

class TrafficMap:
    def __init__(self, canvas, width, height, traffic_points):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.cell_size = 16  # Reduced cell size by 20%
        self.map = [[' ' for _ in range(width)] for _ in range(height)]
        self.rectangles = [[None for _ in range(width)] for _ in range(height)]
        self.road_rows = [0] + [i[1] for i in traffic_points] # Rows containing traffic lights (roads)
        self.road_cols = [0] + [i[0] for i in traffic_points]  # Columns containing traffic lights (roads)
    
    def display(self):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                color = 'black'  # Default color for not-roads
                if y in self.road_rows or x in self.road_cols:
                    color = 'gray'  # Roads are grey
                if (x, y) == (0, 0) or (x, y) == (ambulance.destination_x, ambulance.destination_y):
                    color = 'gray'  # 0th row, 0th column, and destination are grey
                if cell == 'A':
                    color = 'white'  # Ambulance color is white
                elif cell == 'D':
                    color = 'blue'  # Destination color is blue
                elif cell == 'G':
                    color = 'green'  # Traffic lights color is green
                elif cell == 'T':
                    color = 'red'  # Traffic points color is red
                self.rectangles[y][x] = self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                                                     (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                                                     fill=color, outline='')
    
    def clear(self):
        for row in self.rectangles:
            for rectangle in row:
                self.canvas.delete(rectangle)

class Ambulance:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.destination_x = 7
        self.destination_y = 11
    
    def move(self, direction):
        if direction == 'right' and self.x < traffic_map.width - 1:
            self.x += 1
        elif direction == 'left' and self.x > 0:
            self.x -= 1
        elif direction == 'up' and self.y > 0:
            self.y -= 1
        elif direction == 'down' and self.y < traffic_map.height - 1:
            self.y += 1

def update_traffic_lights(ambulance):
    # Determine the direction of the ambulance relative to the destination
    for y in range(traffic_map.height):
        for x in range(traffic_map.width):
            if traffic_map.map[y][x] == 'T':
                if direction == 'down' and ambulance.x == x and ambulance.y - y == -1:
                    traffic_map.map[y][x] = 'G'
                elif direction == 'up' and ambulance.x == x and ambulance.y - y == 1:
                    traffic_map.map[y][x] = 'G'
                elif direction == 'right' and ambulance.y == y and ambulance.x - x == -1:
                    traffic_map.map[y][x] = 'G'
                elif direction == 'left' and ambulance.y == y and ambulance.x - x <= 1:
                    traffic_map.map[y][x] = 'G'
                else:
                    traffic_map.map[y][x] = 'T'
    traffic_map.map[ambulance.destination_y][ambulance.destination_x] = 'D'

def check_game_status(ambulance):
    if abs(ambulance.x - ambulance.destination_x) <= 1 and abs(ambulance.y - ambulance.destination_y) <= 1:
        print("Ambulance has reached the destination!")
        root.quit()
    
direction = '' 

def key_pressed(event):
    global direction

    next_x, next_y = ambulance.x, ambulance.y

    # Calculate the coordinates of the next cell based on the direction
    if event.keysym == 'Up':
        direction = "up"
        next_y -= 1
    elif event.keysym == 'Down':
        direction = "down"
        next_y += 1
    elif event.keysym == 'Left':
        direction = "left"
        next_x -= 1
    elif event.keysym == 'Right':
        direction = "right"
        next_x += 1

    # Check if the next cell is within the canvas boundaries
    if 0 <= next_x < traffic_map.width and 0 <= next_y < traffic_map.height:
        # Check the color of the next cell
        next_cell_color = canvas.itemcget(traffic_map.rectangles[next_y][next_x], 'fill')

        # If the next cell color is not black, move the ambulance
        if next_cell_color != 'black':
            traffic_map.map[ambulance.y][ambulance.x] = 'S'
            ambulance.move(direction)
            update_traffic_lights(ambulance)
            traffic_map.map[ambulance.y][ambulance.x] = 'A'
            traffic_map.clear()
            traffic_map.display()
            check_game_status(ambulance)


# Create the Tkinter window
root = tk.Tk()
root.title("Ambulance Traffic Relief System")

# Create the canvas
canvas_width = 480  # Canvas width
canvas_height = 480  # Canvas height
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='black')  # Set canvas background to black
canvas.pack()

# Creating traffic points
traffic_points = [(7, 5), (15, 15), (10, 7), (3, 12)]  # Example traffic points

# Initialize the traffic map and ambulance
width = 30  # Number of cells in width
height = 30  # Number of cells in height
traffic_map = TrafficMap(canvas, width, height, traffic_points)
ambulance = Ambulance(0, 0)

for point in traffic_points:
    traffic_map.map[point[1]][point[0]] = 'T'

# Bind arrow key events
root.bind('<Key>', key_pressed)

# Start the main loop
update_traffic_lights(ambulance)
traffic_map.map[ambulance.y][ambulance.x] = 'A'
traffic_map.map[ambulance.destination_y][ambulance.destination_x] = 'D'
traffic_map.display()

root.mainloop()
