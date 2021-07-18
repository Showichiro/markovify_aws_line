# markovify_aws_line

- aws lambda にデプロイして使える line_bot 用の発言生成・送信機能のソースコードです(Python3.8 で作りました)
- layer に boto3,markovify,linebot を追加する必要があり
- また S3 上に markovify を利用した学習済みモデルをアップロードする必要あり
- S3 を利用するので S3 の Role をつける必要あり
- 生成数によってはタイム・アウトする可能性があるので関数の実行時間を伸ばしてやる必要あるかもです
