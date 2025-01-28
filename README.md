# **ChanGather**

## **Introduction**
ChanGather is an open-source tool designed to **identify and map Panchan malware relay networks**. This project is for **educational purposes only**, created to analyze malicious infrastructures used by the Panchan malware. **The tool is not intended for malicious or illegal use.**

I am not a professional cybersecurity expert but someone who is passionate about cybersecurity and enjoys exploring malware mechanisms. This project represents my curiosity and desire to learn while sharing knowledge with the community.

---

## **Main Features**
- **Relay Mapping**: Discovers other relays from a starting IP and port, recursively mapping the Panchan network.
- **IP Extraction**: Parses relay responses to extract all associated IP addresses.
- **Queue-Based Exploration**: Ensures efficient processing of all discovered relays while avoiding duplicates.
- **Live Updates**: Displays the currently processed IP and the queue length in real-time.
- **Exploration Statistics**: Summarizes the total relays discovered and visited at the end of the scan.
- **Output File Support**: Saves all discovered IP addresses to an external file for further analysis.

---

## **Prerequisites**
Before using ChanGather, ensure you have the following:

### **Required Software**
- **Python 3.8+**

### **Python Modules**
The script uses standard Python libraries:
- `re`
- `socket`
- `ipaddress`
- `sys`

No external dependencies are required.

---

## **Installation**
1. Clone the repository from GitHub:
   ```bash
   > git clone https://github.com/redrabytes/changather.git
   > cd changather
   ```

2. Make the script executable:
   ```bash
   > chmod +x changather.py
   ```

---

## **Usage**
### **Command**
Run the tool with the following command:
```bash
> ./changather.py <IP> <PORT> <OUTPUT_FILE>
```

### **Parameters**
- `<IP>`: The starting IP address of the suspected Panchan relay (e.g., `192.168.1.100`).
- `<PORT>`: The port number to connect to (e.g., `8080`).
- `<OUTPUT_FILE>`: The file where all discovered IPs will be saved (e.g., `relays.txt`).

### **Example**
```bash
> ./changather.py 192.168.1.100 8080 relays.txt
```

### **Output**
- **Real-Time Logs**: Displays the last processed IP address and the queue length during the scan.
- **Final Statistics**: Provides a summary of:
  - Total unique IPs visited.
  - Location of the output file containing all extracted relay IPs.

---

## **How It Works**
1. **Initial Connection**: The tool connects to the specified IP and port using a TCP socket.
2. **Data Analysis**: If the response contains the keyword `pan-chan`, the tool extracts all IP addresses from the response.
3. **Recursive Discovery**: New IPs are added to a queue and recursively explored, mapping the relay network.
4. **Output Saving**: All extracted IPs are written to the specified output file.
5. **Completion**: The scan finishes when the queue is empty, and a summary of discovered relays is provided.

---

## **Disclaimer**
ChanGather is designed **for educational and research purposes only**. I am not responsible for any misuse or illegal activities conducted with this tool. Always ensure compliance with your local laws regarding network analysis and cybersecurity research.

---

## **Contributions**
I am open to feedback and contributions to improve this project. Since I am not a professional developer, suggestions, bug reports, and pull requests are highly appreciated to make the code more robust and efficient.

---

## **Contact**
If you have any questions or ideas, feel free to reach out to me via GitHub or Twitter.
