# Star-Trek-GPT-2
## GPT-2 Fine-tuned on The Original Series Episode Scripts

TOS episode scripts from http://www.chakoteya.net/
Fine-tuning/Generation/Pretrained GPT-2 via Huggingface's Transformers!



To train: 

```
python fine_tune.py --eval_data_file dev.txt --train_data_file train.txt --model_type gpt2  --model_name_or_path gpt2  --config_name gpt2 --output_dir star_trek --do_train                
```

To test:
```
python fine_tune.py --eval_data_file dev.txt --train_data_file train.txt --model_type gpt2  --model_name_or_path gpt2  --config_name gpt2 --output_dir star_trek --do_eval ----eval_all_checkpoints
```

To generate text:
```

```

## TODO:
-upload pretrained models
-host online demo
