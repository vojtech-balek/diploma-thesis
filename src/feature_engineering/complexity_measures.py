import pandas as pd
import json

def get_length(df, columns):
    if isinstance(columns, str):
        columns = [columns]
    for col in columns:
        df[f'len_{col}'] = df[col].astype(str).str.len()
    return df

def get_modalities(df, col='question'):
    def extract_types(q_str):
        if pd.isna(q_str) or not isinstance(q_str, str):
            return []
        try:
            blocks = json.loads(q_str)
            types = set()
            if isinstance(blocks, list):
                for block in blocks:
                    if isinstance(block, list) and len(block) > 0:
                        b_type = block[0]
                        # Handling 'code64' as 'code' as it's just base64 encoded
                        if b_type == 'code64':
                            b_type = 'code'
                        types.add(b_type)
            return list(types)
        except Exception:
            return []
            
    df[col + '_item_form'] = df[col].apply(extract_types)
    return df

def get_item_metrics(df, dataset_name):
    import os
    logs_df = pd.DataFrame()
    base_path = f'../../data/raw/logs/{dataset_name}'
    
    for dirpath, dirnames, files in os.walk(base_path):
        for file in files:
            temp_df = pd.read_csv(os.path.join(dirpath, file), encoding='utf-8')
            logs_df = pd.concat([logs_df, temp_df], axis=0)

    if logs_df.empty or 'item' not in logs_df.columns:
        metrics_df = pd.DataFrame(columns=['item', 'median_response_time', 'error_rate', 'number_of_occurrences'])
    else:
        response_time = pd.to_numeric(logs_df.get('responseTime'), errors='coerce')
        correct_numeric = pd.to_numeric(logs_df.get('correct'), errors='coerce')

        metrics_df = (
            logs_df.assign(responseTime_num=response_time, correct_num=correct_numeric)
            .groupby('item', dropna=False)
            .agg(
                median_response_time=('responseTime_num', 'median'),
                correct_rate=('correct_num', 'mean'),
                number_of_occurrences=('correct_num', 'size'),
            )
            .reset_index()
        )
        metrics_df['error_rate'] = 1 - metrics_df['correct_rate']
        metrics_df = metrics_df.drop(columns=['correct_rate'])
    
    df = df.merge(metrics_df, how='left', left_on='id_x', right_on='item')
    return df

def process_math():
    math_df = pd.read_csv('../../data/processed/math.csv', delimiter=';')
    math_df = get_length(math_df, ['question_decoded', 'correct_decoded'])
    math_df = get_modalities(math_df, col='question')
    math_df = get_item_metrics(math_df, 'math')

    math_df.to_csv('../../data/feature_engineering/complexity_measures/math.csv', encoding='utf-8', sep=';', index=False)


def process_inf():
    inf_df = pd.read_csv('../../data/processed/informatics.csv', delimiter=';')
    inf_df = get_length(inf_df, ['question_decoded', 'correct_decoded'])
    inf_df = get_modalities(inf_df, col='question')
    inf_df = get_item_metrics(inf_df, 'informatics')

    inf_df.to_csv('../../data/feature_engineering/complexity_measures/informatics.csv', encoding='utf-8', sep=';', index=False)

def process_cs():
    pass

def process_eng():
    pass

if __name__ == '__main__':
    process_math()
    process_inf()
    process_cs()
    process_eng()