# Input color from user
signal = input("Enter the signal color (Red/Yellow/Green): ").strip().lower()
# Check conditions
if signal == "red":
    print("STOP 🚦")
elif signal == "yellow":
    print("STAY / WAIT ⚠️")
elif signal == "green":
    print("GO ✅")
else:
    print("Invalid color! Please enter Red, Yellow, or Green.")


# Output :
#Enter the signal color (Red/Yellow/Green): Red
#STOP 🚦