use std::fs;

fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename)
            .expect("Something went wrong reading the file");
    let mut fuel_total = 0;
    for element in contents.trim().split("\n") {
        let mass = element.parse::<i32>().unwrap();
        let fuel = (mass / 3) - 2;
        fuel_total += fuel;
    }

    println!("{}", fuel_total);
}
