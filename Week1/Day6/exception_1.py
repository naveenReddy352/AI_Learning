try:
    file = open('logs.txt','r')
    error_count = 0
    warning_count = 0

    for line in file:
        if 'ERROR' in line:
            error_count += 1
        if 'WARNING' in line:
            warning_count += 1
    
    print('Error Count:', error_count)
    print('Warning Count:', warning_count)

    file.close()

except FileNotFoundError:
    print('Log file not found')
except Exception as e:
    print('Unexpected error:',e)
finally:
    print('Analysis complete.')
