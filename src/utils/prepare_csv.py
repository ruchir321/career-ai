import subprocess

script_path = "./update_apping_data.sh"

result = subprocess.run(
    [script_path],
    capture_output=True,
    text=True
)

