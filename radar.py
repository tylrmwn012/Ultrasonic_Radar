import matplotlib.pyplot as plt
import numpy as np

def graphScreen(planes, plane_angles):
    categories = ['0°', '30°', '60°', '90°', '120°', '150°', '170°', '200°', '230°', '260°', '290°', '320°']
    num_vars = len(categories)
    
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(facecolor='black', figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.canvas.manager.set_window_title("Radar Sensor")
    ax.set_facecolor('black')
    ax.grid(True, color="green")

    ax.spines['polar'].set_edgecolor(color='green')
    ax.spines['polar'].set_linewidth(2)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories, color="green")
    ax.set_ylim(0, 10)
    ax.set_rlabel_position(0)

    ax.scatter(plane_angles, planes, marker='^', color='white')

    plt.show()

planes = [7, 9, 6, 1, 8] 
plane_degrees = [10, 200, 95, 190, 270]  
plane_angles = np.radians(plane_degrees)

graphScreen(planes, plane_angles)
