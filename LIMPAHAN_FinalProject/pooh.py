import turtle

def draw_image(coordinates, fill_color):
    turtle.speed(0) 
    turtle.pu()  
    turtle.title("Winnie the Pooh") # Dont forget to give the lovely Xi Jing Ping a kiss

    if coordinates:
        turtle.goto(coordinates[0]) 
        turtle.pd()  
        turtle.ht()
        turtle.fillcolor(fill_color)  
        turtle.begin_fill()  
        for coordinate in coordinates:
            x, y = coordinate
            turtle.goto(x, y)
        turtle.end_fill()  

    turtle.pu()  
    turtle.home()    
    turtle.pd() 

def draw_images_from_files(file_colors):
    for fname, fill_color in file_colors.items():
        with open(fname, 'r') as file:
            fill_color = file.readline().strip()
            fcoordinates = [tuple(map(float, line.strip().split(','))) for line in file]
            draw_image(fcoordinates, fill_color)
    turtle.done()

file_colors = {
    'coordinates/d1': '#daa520',
    'coordinates/d2': '#daa520',   
    'coordinates/d3': 'black',
    'coordinates/d4': 'black',
    'coordinates/d5': 'black',
    'coordinates/d6': 'black',
    'coordinates/d7': 'black',
    'coordinates/d8': 'black',
    'coordinates/d9': 'black',
    'coordinates/o1': 'pink',
    'coordinates/o2': 'black',
    'coordinates/o3': 'black',
    'coordinates/o4': 'black',
    'coordinates/o5': 'black',
    'coordinates/o6': 'red',
    'coordinates/o7': 'red',
    'coordinates/o8': 'red',
    'coordinates/o9': 'red',
    'coordinates/g1': '#daa520',
    'coordinates/g2': '#daa520',
    'coordinates/g3': '#daa520',
}
draw_images_from_files(file_colors)