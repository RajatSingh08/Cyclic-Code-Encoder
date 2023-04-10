from django.shortcuts import render
from django.contrib import messages
import random


def inputPage(request):
    return render(request, 'ENCODER/input.html')


def outputPage(request):
    if request.method == 'POST':
        n = request.POST.get('n')
        try:
            n = int(n)
        except ValueError:
            messages.error(request, 'n must be an integer')
            return render(request, 'ENCODER/input.html')
        
        k = request.POST.get('k')
        try:
            k = int(k)
        except ValueError:
            messages.error(request, 'k must be an integer')
            return render(request, 'ENCODER/input.html')
        
        q = request.POST.get('q')
        try:
            q = int(q)
        except ValueError:
            messages.error(request, 'q must be an integer')
            return render(request, 'ENCODER/input.html')
        
        if n <= k:
            messages.error(request, 'n must be greater than k')
            return render(request, 'ENCODER/input.html')
        
        if k < 1:
            messages.error(request, 'k must be positive integer')
            return render(request, 'ENCODER/input.html')
        
        if q < 1:
            messages.error(request, 'q must be positive integer')
            return render(request, 'ENCODER/input.html')
        
        if q > 9:
            messages.error(request, 'q must be ∈ [1, 9]')
            return render(request, 'ENCODER/input.html')
        
        data = request.POST.get('data')

        if len(data)!=k:
            messages.error(request, 'Message length must be equal to k')
            return render(request, 'ENCODER/input.html')
        
        for i in range(k):
            ch = data[i]
            try:
                ch = int(ch)
            except ValueError:
                messages.error(request, f'Invalid Data! Must be integers ∈ [0, {q-1}]')
                return render(request, 'ENCODER/input.html')
            
            if not 0 <= ch < q:
                messages.error(request, f'Invalid Data! Must be integers ∈ [0, {q-1}]')
                return render(request, 'ENCODER/input.html')


        mssg = [int(char) for char in data]
        # Perform encoding using (n, k) cyclic codes
        generator_polynomial = [random.randint(
            0, q-1) for i in range(n - k + 1)]
        g_length = len(generator_polynomial)  # degree of generator polynomial
        encoded = generator_polynomial  # Make a copy of the input data.
        # Add zeros to the end of the generator_polynomial to make it of size n for generating generator matrix.
        for i in range(n - g_length):
            encoded.append(0)
        generator_matrix = []
        for i in range(k):
            generator_matrix.append(encoded)
            encoded = encoded[-1:] + encoded[:-1]
        # print(generator_matrix)
        codeword = [0 for _ in range(n)]
        for j in range(len(generator_matrix[0])):
            t = 0
            for i in range(k):
                t = (t + (mssg[i] * generator_matrix[i][j]) % q) % q
            codeword[j] = t
        output = ''.join(str(n) for n in codeword)
        generator = []
        for i in range(n-k+1):
            if generator_polynomial[i] == 0:
                continue
            if i == 0:
                generator.append(f"{generator_polynomial[i]}")
            elif i==1:
                generator.append(f"{generator_polynomial[i]}*x")
            else:
                generator.append(f"{generator_polynomial[i]}*x^{i}")
        g = " + ".join(generator)
        # return the encoded data
        context = {'n': n, 'k': k, 'q': q, 'data': data,
                'g': g, 'output': output}
        return render(request, 'ENCODER/output.html', context)