#![allow(unused)]

use std::fs::File;
use std::io::{BufRead, BufReader};

fn read_file(path: &str) -> Vec<String> {
    let mut input: Vec<String> = Vec::new();
    println!("Reading data from: {path}");
    let input_file: File =
        File::open(path).expect(format!("Error while reading file {path}").as_str());
    let buffered: BufReader<File> = BufReader::new(input_file);
    for line in buffered.lines() {
        input.push(line.expect("Error in reading line from file"));
    }
    input
}

/// Part one of day 1 of 2023 Advent of Code
fn part_one(path: &str) {
    let parse_number = |number: &String| number.parse::<i32>().expect("Error while parsing");
    let input: Vec<String> = read_file(path);

    let mut calibration_value: i32;
    let mut calibration_values_sum: i32 = 0;
    for code in input {
        let mut number: String = code.chars().filter(|c| c.is_numeric()).collect::<String>();
        print!("{code}");
        calibration_value = match number.len() {
            0 => 0,
            1 => parse_number(&number) * 10 + parse_number(&number),
            2 => parse_number(&number),
            3.. => {
                while number.len() > 2 {
                    number.remove(1);
                }
                parse_number(&number)
            }
        };
        calibration_values_sum += calibration_value;
        println!(" : {calibration_value} --> {calibration_values_sum}");
        number.clear();
    }
    println!("Calibration values sum: {calibration_values_sum}");
}

/// Part two of day 1 of 2023 Advent of Code
fn part_two(path: &str) {
    // Closure for parsing numbers
    let parse_number: fn(&String) -> i32 =
        |number: &String| -> i32 { number.parse::<i32>().expect("Error while parsing") };
    // Array of text numbers
    // let text_nums: [&str;9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let text_nums: &str = "one,two,three,four,five,six,seven,eight,nine";
    let mut calibration_values_sum: i32 = 0;
    let mut cal_vals: Vec<(usize, i32)> = Vec::new();
    for mut code in read_file(path) {
        print!("{code}");
        let mut i: usize = 0;
        for c in code.chars() {
            if c.is_numeric() {
                cal_vals.push((i, parse_number(&c.to_string())));
            }
            i += 1;
        }
        i = 1;
        for n in text_nums.split(',') {
            let mut j: usize = 0;
            // loop if more than 1 occurence of a number
            loop {
                match code.split_at(j).1.to_string().find(n) {
                    Some(index) => {
                        cal_vals.push((index + j, i as i32));
                        j += index + n.len();
                    }
                    None => break,
                };
            }
            i += 1;
        }
        let calibration_value: i32 = match cal_vals.len() {
            0 => 0,
            1 => cal_vals[0].1 * 10 + cal_vals[0].1,
            n => {
                cal_vals.sort_by_key(|k: &(usize, i32)| k.0);
                cal_vals[0].1 * 10 + cal_vals[n - 1].1
            }
        };
        calibration_values_sum += calibration_value;
        println!(
            " : {} --> {}",
            calibration_value, calibration_values_sum
        );
        cal_vals.clear();
    }
    println!("Calibration values sum: {calibration_values_sum}");
}

fn main() {
    // let path: &str = "test.txt";
    // let path: &str = "test2.txt";
    let path: &str = "calibration_file.txt";
    // part_one(path);
    part_two(path);
}
