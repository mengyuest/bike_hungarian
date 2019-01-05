# Hungarian method for people-bikes matching

## Usage:
1. Generate data (or you can just use `data.txt`): `python3 data_mocker.py --data_file datarand.txt --height 10 --width 8 --num_people 6 --num_bikes 20`
2. Test brute-force method(using DFS): `python3 solver.py --method hungarian --data_file datarand.txt`
3. Test hungarian method(using Kuhn–Munkres method): `python3 solver.py --method hungarian --data_file datarand.txt`

