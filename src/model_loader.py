import tflite_runtime.interpreter as tflite

def load_whisper_model(model_path):
    """Load the Whisper model from Qualcomm AI Hub."""
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

MODEL_PATH = "models/whisper_base_en-whisperdecoder.tflite"
whisper_model = load_whisper_model(MODEL_PATH)
