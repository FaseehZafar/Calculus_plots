# Import the math module to access mathematical functions like sqrt()
import math

# Function to display introductory information about the software and team
def display_intro():
    # Print decorative header line
    print("=============================================")
    # Print software house name
    print("     WOODTECH OPTIMIZATION SOLUTIONS")
    # Print team header
    print("     Programming Team:")
    # Print each team member with their ID
    print("     1. Muhammad Faseeh Zafar (ID: 24i-2529)")
    print("     2. Abdullah Khan (ID: 24i-2563)")
    print("     3. Huzaifa Rehman (ID: 24i-2554)")
    # Print decorative footer line
    print("=============================================")
    # Wait for user to press Enter before continuing
    input("Press Enter to continue...")

# Function to calculate optimal beam dimensions from log diameter
def optimize_beam(diameter):
    # Calculate optimal width using the formula: b = d/sqrt(3)
    # This comes from the calculus solution to maximize beam strength
    width = diameter / math.sqrt(3)
    
    # Calculate corresponding height using Pythagorean theorem:
    # h = sqrt(d^2 - b^2) since the rectangle fits in the circular log
    height = math.sqrt(diameter**2 - width**2)
    
    # Return both dimensions as floating point numbers
    return width, height

# Main function that controls program flow
def main():
    # Display introductory information first
    display_intro()
    
    # Start infinite loop to handle multiple calculations
    while True:
        try:
            # Prompt user to enter log diameter
            d = float(input("\nEnter the diameter of the round log (in inches): "))
            
            # Validate input is positive
            if d <= 0:
                print("Diameter must be positive. Try again.")
                # Skip rest of loop iteration if invalid
                continue
        except ValueError:
            # Handle case where input isn't a number
            print("Invalid input. Please enter a number.")
            # Skip rest of loop iteration if invalid
            continue

        # Calculate optimal dimensions
        width, height = optimize_beam(d)
        
        # Display results with 2 decimal places
        print("\nOptimal Dimensions of Strongest Rectangular Beam:")
        print(f"Width  = {width:.2f} inches")
        print(f"Height = {height:.2f} inches")

        # Ask user if they want to perform another calculation
        again = input("\nDo you want to run another query? (y/n): ").strip().lower()
        
        # Check if user wants to quit
        if again != 'y':
            # Print goodbye message
            print("Thank you for using WoodTech Optimization Solutions. Goodbye!")
            # Exit the infinite loop
            break

# Standard Python idiom to check if this script is being run directly
if __name__ == "__main__":
    # If so, execute the main function
    main()
