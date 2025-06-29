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

        plt.ion()  # interactive mode

        fig, ax = plt.subplots(facecolor='black', figsize=(6, 6), subplot_kw=dict(polar=True))
        fig.canvas.manager.set_window_title("Radar Sensor")
        ax.set_facecolor('green')
        ax.grid(True, color="limegreen")

        ax.spines['polar'].set_edgecolor(color='limegreen')
        ax.spines['polar'].set_linewidth(2)

        ax.set_theta_offset(np.pi / 2)
        ax.set_thetagrids(np.degrees(angles[:-1]), categories, color="limegreen")
        ax.set_ylim(0, 40)
        ax.tick_params(axis='y', colors="limegreen", labelsize=8)
        ax.set_rlabel_position(0)

        ax.set_theta_zero_location('E')
        ax.set_thetamin(0)
        ax.set_thetamax(180)

        scatter = ax.scatter([], [], marker='^', color='red')

        (line,) = ax.plot([], [], color='red', linewidth=1)

        return fig, ax, scatter, line

    def getDegrees(serialInst):
        if serialInst.in_waiting:
            packet = serialInst.readline()
            degree = packet.decode('utf').strip()
            print(degree)
            return int(degree)
        return None

    # Get list of ports
    ports = serial.tools.list_ports.comports()
    portList = [port.device for port in ports]

    # Show ports with numbers
    for i, port in enumerate(portList):
        print(f"{i}: {port}")

    # User picks by index
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

    # Set up serial
    serialInst = serial.Serial()
    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()

    print(f"Connected to {portVar}")

    # Initialize plot
    fig, ax, scatter, line = graphScreen()

    plane_degrees = []
    planes = []

    while True:
        degree = getDegrees(serialInst)
        if degree is not None:
            plane_degrees.append(degree)
            planes.append(36)  # constant radius, or change as needed

            angle_rad = np.radians(degree)

            # Convert to radians
            plane_angles = np.radians(plane_degrees)

            # Update scatter data
            scatter.set_offsets(np.c_[plane_angles, planes])

            # 🔹 Added: update line data to go from center to edge
            angle_rad = plane_angles[-1]
            line.set_data([angle_rad, angle_rad], [0, 40])

            plt.draw()
            plt.pause(0.001)
            plt.legend(loc="lower left")

            plane_degrees.pop()
            planes.pop()

main()