from spleeter.separator import Separator

# 3つのトラック（ボーカルと伴奏とドラム）に分離するためのセパレータを作成
separator = Separator('spleeter:3stems')

# 分離したいオーディオファイルのパス
audio_file = 'file name'

# 分離処理を実行し、出力を指定されたフォルダに保存
separator.separate_to_file(audio_file, 'file name')