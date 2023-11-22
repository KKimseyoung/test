from flask import Flask, render_template, request
import mne
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def get_data(path):
    eeg_data = mne.io.read_raw_brainvision(path, preload=True)
    eeg_data = eeg_data.pick_types(eeg=True)

    data_0 = list(eeg_data.get_data()[0, :300])
    data_1 = list(eeg_data.get_data()[1, :300])
    data_2 = list(eeg_data.get_data()[2, :300])
    data_3 = list(eeg_data.get_data()[3, :300])
    data_4 = list(eeg_data.get_data()[4, :300])
    data_5 = list(eeg_data.get_data()[5, :300])
    data_6 = list(eeg_data.get_data()[6, :300])
    data_7 = list(eeg_data.get_data()[7, :300])
    data_8 = list(eeg_data.get_data()[8, :300])

    data_0_str = ",".join(map(str, data_0))
    data_1_str = ",".join(map(str, data_1))
    data_2_str = ",".join(map(str, data_2))
    data_3_str = ",".join(map(str, data_3))
    data_4_str = ",".join(map(str, data_4))
    data_5_str = ",".join(map(str, data_5))
    data_6_str = ",".join(map(str, data_6))
    data_7_str = ",".join(map(str, data_7))
    data_8_str = ",".join(map(str, data_8))

    return data_0_str, data_1_str, data_2_str, data_3_str, data_4_str, data_5_str, data_6_str, data_7_str, data_8_str

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            eeg_data_0, eeg_data_1, eeg_data_2, eeg_data_3, eeg_data_4, eeg_data_5, eeg_data_6, eeg_data_7, eeg_data_8 = get_data(file_path)
            return render_template('index.html', eeg_data_0=eeg_data_0, eeg_data_1=eeg_data_1, eeg_data_2=eeg_data_2, eeg_data_3=eeg_data_3, eeg_data_4=eeg_data_4, eeg_data_5=eeg_data_5, eeg_data_6=eeg_data_6, eeg_data_7=eeg_data_7, eeg_data_8=eeg_data_8)

    return render_template('index.html', eeg_data_0='', eeg_data_1='', eeg_data_2='', eeg_data_3='', eeg_data_4='', eeg_data_5='', eeg_data_6='', eeg_data_7='', eeg_data_8='')

if __name__ == '__main__':
    app.run(debug=True)
