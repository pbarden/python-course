def seconds_to_jiffies(user_seconds):
    answer = float(user_seconds) * 100.0
    return answer

if __name__ == '__main__':
    j_pop = float(input())
    jiffy_p = seconds_to_jiffies(j_pop)
    print('%.2f' % jiffy_p)