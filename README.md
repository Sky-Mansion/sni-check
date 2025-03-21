# SNI Checker

This Python script checks the validity of Server Name Indication (SNI) hosts by establishing an SSL connection and measuring their latency. It reads a list of SNIs from a file, tests their connectivity, and saves the working SNIs to a separate file.

## Features
- Reads SNIs from `host.txt`
- Checks if an SNI is valid using SSL
- Measures latency for working SNIs
- Saves valid SNIs to `working_sni.txt`

## Requirements
- Python 3

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Sky-Mansion/sni-check.git
   cd sni-check
   ```
2. Ensure you have Python installed.

## Usage
1. Add a list of SNIs (one per line) in `host.txt`.
2. Run the script:
   ```sh
   python hostck.py
   ```
3. The working SNIs will be saved in `working_sni_zoom.txt`.

## File Structure
```
📂 sni-check
├── host.txt             # Input file containing SNIs
├── working_sni.txt      # Output file with working SNIs
├── hostck.py            # Main script
├── README.md            # Documentation
```

## Example
```
Testing SNI: example.com...
[✔] example.com works! Latency: 120.5ms
[✘] invalid-sni.com failed.

✅ Working SNIs saved to working_sni_zoom.txt
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve the script!

---
Made with ❤️ by dilshan

