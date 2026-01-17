if __name__ == "__main__":
    while True:
        try:
            arr = list(map(float, input().split()))
            if arr[0] == arr[4] and arr[1] == arr[5]:
                print(f"{(arr[2]-arr[0]+arr[6]) :.3f} {(arr[3]-arr[1]+arr[7]):.3f}")
            elif arr[0] == arr[6] and arr[1] == arr[7]:
                print(f"{(arr[4]-arr[0]+arr[2]) :.3f} {(arr[5]-arr[1]+arr[3]):.3f}")
            elif arr[2] == arr[4] and arr[3] == arr[5]:
                print(f"{(arr[0]-arr[2]+arr[6]) :.3f} {(arr[1]-arr[3]+arr[7]):.3f}")
            elif arr[2] == arr[6] and arr[3] == arr[7]:
                print(f"{(arr[0]-arr[2]+arr[4]) :.3f} {(arr[1]-arr[3]+arr[5]):.3f}")
        except EOFError:
            break