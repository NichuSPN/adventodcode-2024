import streamlit as st

INPUT_FILE_NAME = "actual.txt"
m, n=103, 101

def updateOneIteration():
    new_points = []
    for i, point in enumerate(st.session_state["points"]):
        xs, ys = point["x"], point["y"]
        [xv, yv] = st.session_state["velocity"][i]
        curr_x = (xs+xv)%n
        curr_y = (ys+yv)%m
        new_points.append({"x": curr_x, "y": curr_y})
    st.session_state["points"]=new_points
    st.session_state["seconds"]+=1

def updateNIterations(num):
    new_points = []
    for i, point in enumerate(st.session_state["points"]):
        xs, ys = point["x"], point["y"]
        [xv, yv] = st.session_state["velocity"][i]
        curr_x = (xs+num*xv)%n
        curr_y = (ys+num*yv)%m
        new_points.append({"x": curr_x, "y": curr_y})
    st.session_state["points"]=new_points
    st.session_state["seconds"]+=num
    
if "velocity" not in st.session_state:
    velocity = []
    points = []
    with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
        for line in file:
            [start, vel] = line.strip().split(' ')
            [xs, ys] = [int(x) for x in start[2:].split(',')]
            points.append({"x": xs, "y": ys})
            velocity.append([int(x) for x in vel[2:].split(',')])
        st.session_state["startSecs"]=6000
        st.session_state["velocity"]=velocity
        st.session_state["points"]=points
        st.session_state["seconds"]=0
        updateNIterations(st.session_state["startSecs"])
        
refreshTop = st.button(label="Next", icon="⏭️")

if refreshTop:
    for i in range(100):
        updateOneIteration()
        st.write(st.session_state["seconds"], "Seconds")
        st.scatter_chart(st.session_state["points"], x="x", y = "y")   
    st.session_state["startSecs"]+=100
    
# install streamlit
# run this using streamlit run ./part2.py
# manually search through for the pattern