use std::fs;

fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename)
            .expect("Something went wrong reading the file");
    let mut fuel_total = 0;
    for element in contents.trim().split("\n") {
        let mass = element.parse::<i32>().unwrap();
        fuel_total += calc_fuel(mass);
    }

    println!("{}", fuel_total);
}

fn calc_fuel(mass: i32) -> i32 {
    let fuel = (mass / 3) - 2;
    if fuel > 0 {
        fuel + calc_fuel(fuel)
    } else {
        0
    }
}
