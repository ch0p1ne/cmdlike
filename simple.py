import subprocess

# Run a simple command
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# Print the output
print(result.stdout)