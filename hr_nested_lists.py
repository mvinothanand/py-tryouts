if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    print(f'Records: {records}')  
    scores = []
    for record in records:
        scores.append(record[1])
        
    print(f'scores: {scores}')
    max_score = max(scores)
    print(f'max score: {max_score}')
    second_largest_score = max([score for score in scores if score < max_score])
    print(f'2nd largest: {second_largest_score}')
    
    second_largest_scorers = sorted([record[0] for record in records if record[1] == second_largest_score])
    print(f'2nd largest scorers: {second_largest_scorers}')
    
    for name in second_largest_scorers:
        print(name)