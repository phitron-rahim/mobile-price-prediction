

import gradio as gr
import numpy as np
import pickle


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_price_range(
    battery_power, blue, clock_speed, dual_sim, fc, four_g,
    int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
    px_width, ram, sc_h, sc_w, talk_time, three_g,
    touch_screen, wifi
):


    battery_per_weight = battery_power / mobile_wt


    input_data = np.array([[
        battery_power, blue, clock_speed, dual_sim, fc, four_g,
        int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
        px_width, ram, sc_h, sc_w, talk_time, three_g,
        touch_screen, wifi, battery_per_weight
    ]])


    pred = model.predict(input_data)[0]

    labels = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost"
    }

    return f"Predicted Price Range: {pred} - {labels[pred]}"

inputs = [
    gr.Number(label="Battery Power (mAh)"),
    gr.Number(label="Bluetooth (0 = No, 1 = Yes)"),
    gr.Number(label="Clock Speed (GHz)"),
    gr.Number(label="Dual SIM (0 = No, 1 = Yes)"),
    gr.Number(label="Front Camera (MP)"),
    gr.Number(label="4G Support (0 = No, 1 = Yes)"),
    gr.Number(label="Internal Memory (GB)"),
    gr.Number(label="Mobile Depth"),
    gr.Number(label="Mobile Weight (g)"),
    gr.Number(label="Number of Cores"),
    gr.Number(label="Primary Camera (MP)"),
    gr.Number(label="Pixel Height"),
    gr.Number(label="Pixel Width"),
    gr.Number(label="RAM (MB)"),
    gr.Number(label="Screen Height"),
    gr.Number(label="Screen Width"),
    gr.Number(label="Talk Time (hours)"),
    gr.Number(label="3G Support (0 = No, 1 = Yes)"),
    gr.Number(label="Touch Screen (0 = No, 1 = Yes)"),
    gr.Number(label="WiFi (0 = No, 1 = Yes)")
]

app = gr.Interface(
    fn=predict_price_range,
    inputs=inputs,
    outputs="text",
    title="Mobile Price Range Predictor",
    description="Enter mobile specifications to predict price range"
)

app.launch(share=True)
