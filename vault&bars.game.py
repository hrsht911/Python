class RaisingCustomBarsError(Exception):
    pass

# Graph layout and search algorithms
maze = {"Start": ["Corridor"], "Corridor": ["Start", "Vault", "Boss"], "Vault": ["Corridor"], "Boss": ["Corridor"]}

def bfs(start, target): # Breadth-First Search
    q = [[start]]
    while q:
        path = q.pop(0)
        if path[-1] == target: return path
        for n in maze[path[-1]]:
            if n not in path: q.append(path + [n])

def dfs(curr, target, visited=None): # Depth-First Search
    if visited is None: visited = set()
    visited.add(curr)
    if curr == target: return [curr]
    for n in maze[curr]:
        if n not in visited:
            res = dfs(n, target, visited)
            if res: return [curr] + res

# Game Loop
room, keys = "Start", 0
while True:
    print(f"\n📍 You are in: {room} | Keys: {keys}/1")
    
    if room == "Boss" and keys < 1:
        try:
            raise RaisingCustomBarsError("🔒 Iron bars block your way! You need 1 key.")
        except RaisingCustomBarsError as e:
            print(e)
            room = "Corridor"
            continue
    elif room == "Boss":
        print("🎉 You defeated the boss and won!")
        break
    
    cmd = input("Go (Corridor/Vault/Boss/Start), [bfs], [dfs], or [quit]: ").strip().title()
    
    if cmd == "Quit": break
    elif cmd == "Bfs": print(f"Shortest path to Boss: {' -> '.join(bfs(room, 'Boss'))}")
    elif cmd == "Dfs": print(f"DFS path to Vault: {' -> '.join(dfs(room, 'Vault'))}")
    elif cmd in maze[room]:
        room = cmd
        if room == "Vault" and keys == 0:
            keys = 1
            print("🔑 You found a key!")
    else:
        print("❌ Can't go there!")