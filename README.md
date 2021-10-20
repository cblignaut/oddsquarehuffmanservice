# Odd square Huffman service
**A service with an odd square number list, huffman encode and huffman decode methods**

## Features
- An odd square number list method that returns a list with odd numbers squared.
- A huffman encode method that returns a huffman encoded string.
- A huffman decode method that returns a huffman decoded string, requires a given or stored frequency table.


## Requirements

Tested with:

* Python: 3.6, Pypy 3.5
* rabbitmq: 3.9
* docker: 20.10
* docker-compose: 1.29

## Installation

1. git clone git@github.com:cblignaut/oddsquarehuffmanservice.git
2. Install python 3.6, docker and docker-compose
3. Go to root directory of cloned repo
4. Run to build docker service container:
```bash
   docker-compose build
```
5. Run to start docker services as a daemon:
```bash
   docker-compose up -d
```

## Usage

### Start nameko shell:
1. Once the docker services are up (see installation)
2. Bash into the docker service:
```bash
   docker exec -ti service bash 
```
3. Run nameko shell:
```bash
   nameko shell --config config.yml
```
### Square odd numbers:
Run the square odd numbers method in the nameko shell:
```bash
   n.rpc.service.square_odd_numbers([1,2,3,4,5])
```
### Huffman encode a list of strings:
Run the huffman encode method in the nameko shell:
```bash
   n.rpc.service.huffman_encode(['test'])
```
### Huffman decode an encoded string:
To decode a huffman encoded string a stored frequency table is required. 
Note: For this example the service will store all encoded strings in memory (this is not a production solution).

Run the huffman decode method in the nameko shell:
   1. For a previously encoded string ('test'):
   ```bash
      n.rpc.service.huffman_decode('010110')
   ```
   2. With a frequency table (this is another option):
   ```bash
      from collections import Counter
      
      frequency_table = Counter("A man")
      
      n.rpc.service.huffman_decode('110101110100', frequency_table)
   ```

## Task

It was a fun open-ended task with a few gotchas (see design decisions). Nameko looks like a good alternative to flask for microservices.  

### Pros: 

- The Nameko & Rabbitmq works well together. 
- Nameko reduce CPU cycle & memory usage to help with scaling
- Easy to monitor and maintain services.

### Cons:

- Increased latency of each call to other non microservice solutions.
- Nameko is less well known with fewer examples and documentation than other microservice python options such as flask.

### Design Decisions:

#### Huffman module
The first options I found was dahuffman & huffman (outdated). 

The dahuffman module looked like a good option but the task requested PyPy. Execution speed is important.

I used the bitarray module before which was written in CPython, I tested the decodetree method and it is faster than dahuffman.

#### Decoding huffman
To decode a huffman string we need a frequency table of the original string. The task didn't specify if we will get a frequency table. 

I decided to create an optional argument for the frequency table but also store the frequency table of the previously encoded strings as a fallback in memory.

```bash
n.rpc.service.huffman_decode('110101110100', OPTIONAL_FREQUENCY_TABLE)
```

    WARNING: WHEN USING THE huffman_decode() METHOD WITHOUT A FREQUENCY TABLE ARGUMENT:

    Ignoring the frequency table argument will return the previous value for an encoded string (requirement). 

    If a different string had the same encoded string then the previous encoded string will be overwritten.

    Currently, the frequency table is stored in memory (scaling risk) and will be lost if the service restart.
    A better solution would be to store the frequency table in a key-value store like redis or always require the client to supply the frequency table.

### Time Management:

Unfortunately I had to do this task while working on assignments for my MEng. Data Science & Machine Learning and my time was limited.

1. I did some research on huffman encoding & decoding 1h
2. Search for a huffman package to use, this took longer than I expected 2h
3. Write tests & tox 1h
4. Coding & cleanup 3h
5. Write README 2h


## Contribution

Please create an issue [New Issue](https://github.com/cblignaut/oddsquarehuffmanservice/issues/new)

## License

See LICENSE file for more information.
     


