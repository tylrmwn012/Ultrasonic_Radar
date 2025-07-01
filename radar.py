import matplotlib.pyplot as plt
import numpy as np
import serial
import serial.tools.list_ports

def main():

    def graphScreen():
        categories = ['0°', '20°', '40°', '60°', '80°', '100°', '120°', '140°', 
                      '160°', '180°', '200', '220', '240', '260', '280', '300', '320', '340']
        num_vars = len(categories)
        
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]

        plt.ion() 

        fig, ax = plt.subplots(facecolor='black', figsize=(6, 6), subplot_kw=dict(polar=True))
        fig.canvas.manager.set_window_title("Radar Sensor")
        ax.set_facecolor('green')
        ax.grid(True, color="limegreen")

        ax.spines['polar'].set_edgecolor(color='limegreen')
        ax.spines['polar'].set_linewidth(2)

        ax.set_theta_offset(np.pi / 2)
        ax.set_thetagrids(np.degrees(angles[:-1]), categories, color="limegreen")
        ax.set_ylim(0, 35)
        ax.tick_params(axis='y', colors="limegreen", labelsize=8)
        ax.set_rlabel_position(0)

        ax.set_theta_zero_location('E')
        ax.set_thetamin(0)
        ax.set_thetamax(180)

        scatter = ax.scatter([], [], marker='^', color='red', label="OBJECT")

        (line,) = ax.plot([], [], color='limegreen', linewidth=1)

        return fig, ax, scatter, line

    def getDegrees(serialInst):
        if serialInst.in_waiting is not None:
            packet = serialInst.readline()
            data = packet.decode('utf').strip()
            print(data)
            return data
        return None

    ports = serial.tools.list_ports.comports()
    portList = [port.device for port in ports]

    for i, port in enumerate(portList):
        print(f"{i}: {port}")

    try:
        index = int(input("Select port number: "))
        if 0 <= index < len(portList):
            portVar = portList[index]
        else:
            print("Invalid selection.")
            exit()
    except ValueError:
        print("Invalid input.")
        exit()

    serialInst = serial.Serial()
    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()

    print(f"Connected to {portVar}")

    fig, ax, scatter, line = graphScreen()

    plane_degrees = [] 
    planes = [] 

    line_degree = []

    while True:
        data = getDegrees(serialInst)
        if data is not None:
            dataList = data.split(',')
            distance = int(dataList[0])
            angle = int(dataList[1])
        else:
            pass

        if distance:

            line_degree.append(angle)

            plane_degrees.append(angle)
            planes.append(distance)

            angle_rad = np.radians(angle)

            plane_angles = np.radians(plane_degrees)
            line_angles = np.radians(line_degree) 

            scatter.set_offsets(np.c_[plane_angles, planes]) 

            angle_rad = line_angles[-1] 
            line.set_data([angle_rad, angle_rad], [0, 35]) 

            plt.draw()
            plt.pause(0.0000000000000001)

            line_degree.pop()
        
            if plane_degrees.count(0) == 1 :
                planes.clear()
                plane_degrees.clear()

main()