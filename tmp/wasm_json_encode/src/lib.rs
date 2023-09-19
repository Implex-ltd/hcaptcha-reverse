use serde::{Serialize, Deserialize};
use wasm_bindgen::prelude::*;

// Define a struct to represent the data
#[derive(Serialize, Deserialize)]
struct MyData {
    uwutext: String,
}

// Expose a function that encodes the data to JSON and returns it as a JS string
#[wasm_bindgen]
pub fn encode_data() -> String {
    let data = MyData {
        uwutext: "hellow".to_string(),
    };

    // Serialize the data to JSON
    let json_string = serde_json::to_string(&data).unwrap();

    json_string
}
