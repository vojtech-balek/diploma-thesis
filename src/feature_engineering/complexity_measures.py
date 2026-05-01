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

def process_math():
    math_df = pd.read_csv('../../data/processed/math.csv', delimiter=';')
    math_df = get_length(math_df, ['question_decoded', 'correct_decoded'])
    math_df = get_modalities(math_df, col='question')

    pass

def process_inf():
    inf_df = pd.read_csv('../../data/processed/informatics.csv', delimiter=';')
    inf_df = get_length(inf_df, ['question_decoded', 'correct_decoded'])
    inf_df = get_modalities(inf_df, col='question')
    pass

def process_cs():
    pass

def process_eng():
    pass

if __name__ == '__main__':
    process_math()
    process_inf()
    process_cs()
    process_eng()