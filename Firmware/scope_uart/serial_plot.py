import serial
import matplotlib.pyplot as plt

PORT = "/dev/tty.usbmodem103"
BAUD = 115200
N = 256

ser = serial.Serial(PORT, BAUD, timeout=1)
print("Serial connected")

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([0]*N)
ax.set_xlim(0, N-1)
ax.set_ylim(0, 3.3)
ax.set_title("STM32 Live Oscilloscope")
ax.set_xlabel("Sample")
ax.set_ylabel("Voltage (V)")
ax.grid(True)

try:
    while True:
        samples = []

        # read until we get a full frame
        while True:
            s = ser.readline().decode("utf-8", errors="ignore").strip()
            if not s:
                continue

            if s == "END":
                if len(samples) == N:
                    break
                else:
                    # bad/partial frame; reset and keep going
                    samples = []
                    continue

            try:
                samples.append(float(s))
                if len(samples) > N:
                    # too many numbers => resync
                    samples = []
            except ValueError:
                pass

        # plot
        line.set_ydata(samples)
        fig.canvas.draw()
        fig.canvas.flush_events()

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    ser.close()
    plt.ioff()
    plt.show()

