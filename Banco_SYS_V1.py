import pandas as pd
from datetime import date

# Function to load the register data from the CSV file
def load_register():
    try:
        register_df = pd.read_csv('contas.csv')
        return register_df
    except FileNotFoundError:
        # If the file doesn't exist, return an empty DataFrame
        return pd.DataFrame(columns=['Nconta', 'Agencia', 'CPF', 'Nome', 'Saldo', 'Movimentos'])

# Function to save the register data to the CSV file
def save_register(register_df):
    register_df.to_csv('contas.csv', index=False)

# Function to add a new register
def add_register(register_df):
    name = input("Nome do cliente: ")
    cpf = int(input("CPF do cliente: "))

    # Find the last ID and auto-increment by 1
    if register_df.empty:
        last_id = 0
    else:
        last_id = register_df['Nconta'].max()
    new_id = last_id + 1

    # Create a new register DataFrame
    new_register = pd.DataFrame({'Nconta': [new_id], 'Agencia': [123], 'CPF': [cpf], 'Nome': [name], 'Saldo': [0], 'Movimentos': ['']})

    # Concatenate the new register DataFrame with the existing register DataFrame
    register_df = pd.concat([register_df, new_register], ignore_index=True)

    print("New register added successfully!")
    return register_df

# Function to consult all registers
def consult_registers(register_df):
    if register_df.empty:
        print("No registers found.")
    else:
        print(register_df)

# Function to delete a register by ID
def delete_register(register_df):
    id_to_delete = int(input("Enter the ID of the register to delete: "))

    # Check if the ID exists in the DataFrame
    if id_to_delete in register_df['Nconta'].values:
        register_df = register_df[register_df['Nconta'] != id_to_delete]
        print("Register deleted successfully!")
    else:
        print("ID not found in the register.")

    return register_df

# Function to add a value to the 'Movimentos' column for a specific 'Nconta' ID
def add_movement(register_df):
    id_to_update = int(input("Enter the ID of the register to update: "))
    movement_type = input("Enter the movement type (1 for plus, 2 for minus): ")
    movement_value = float(input("Enter the movement value: "))

    # Check if the ID exists in the DataFrame
    if id_to_update in register_df['Nconta'].values:
        today_date = date.today().strftime("%Y-%m-%d")

        # Update the 'Saldo' column based on the movement type
        if movement_type == '1':
            register_df.loc[register_df['Nconta'] == id_to_update, 'Saldo'] += movement_value
            movement = f"Plus: +{movement_value}"
        elif movement_type == '2':
            register_df.loc[register_df['Nconta'] == id_to_update, 'Saldo'] -= movement_value
            movement = f"Minus: -{movement_value}"
        else:
            print("Invalid movement type. No changes made.")
            return register_df

        # Update the 'Movimentos' column with the movement details
        register_df.loc[register_df['Nconta'] == id_to_update, 'Movimentos'] += f"{movement} ({today_date})\n"
        print("Movement added successfully!")
    else:
        print("ID not found in the register.")

    return register_df

# Main program
def main():
    # Load the register data
    register_df = load_register()

    # Menu loop
    while True:
        print("\n-- Register System Menu --")
        print("1. Add new register")
        print("2. Consult all registers")
        print("3. Delete a register by ID")
        print("4. Add movement for a specific Nconta ID")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            register_df = add_register(register_df)
        elif choice == '2':
            consult_registers(register_df)
        elif choice == '3':
            register_df = delete_register(register_df)
        elif choice == '4':
            register_df = add_movement(register_df)
        elif choice == '5':
            save_register(register_df)
            print("Register data saved successfully. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()
