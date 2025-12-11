def dfs(graph, current, target, memo):
    if current == target:
        return 1

    if current in memo:
        return memo[current]

    path_count = 0

    for vertex in graph.get(current, []):
        path_count += dfs(graph, vertex, target, memo)

    memo[current] = path_count

    return path_count


graph = {}

with open("./input.txt") as f:
    for line in f:
        devices = line.strip().split()

        graph[devices[0][:-1]] = devices[1:]


total_valid_paths_you_out = dfs(graph, "you", "out", {})

svr_dac = dfs(graph, "svr", "dac", {})
dac_fft = dfs(graph, "dac", "fft", {})
fft_out = dfs(graph, "fft", "out", {})

svr_fft = dfs(graph, "svr", "fft", {})
fft_dac = dfs(graph, "fft", "dac", {})
dac_out = dfs(graph, "dac", "out", {})

valid_paths_svr_dac_fft_out = svr_dac * dac_fft * fft_out
valid_paths_svr_fft_dac_out = svr_fft * fft_dac * dac_out

total_valid_paths_svr_out = valid_paths_svr_dac_fft_out + valid_paths_svr_fft_dac_out

print(f"Part 1: {total_valid_paths_you_out}")
print(f"Part 2: {total_valid_paths_svr_out}")
