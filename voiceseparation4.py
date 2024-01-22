from spleeter.separator import Separator

# 4つのトラック（ボーカルと伴奏とドラムとその他の楽器）に分離するためのセパレータを作成
separator = Separator('spleeter:4stems')

# 分離したいオーディオファイルのパス
audio_file = 'file name'

# 分離処理を実行し、出力を指定されたフォルダに保存
separator.separate_to_file(audio_file, 'file name')