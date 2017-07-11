def main():
    score1, score2, score3, score4 = map(float, input().split())

    media = (score1 * 2 + score2 * 3 + score3 * 4 + score4) / 10
    print('Media: {:.1f}'.format(media))

    if media >= 7.0:
        print('Aluno aprovado.')
    elif media < 5.0:
        print('Aluno reprovado.')
    else:
        exam = float(input())
        print('Aluno em exame.')
        print('Nota do exame: {:.1f}'.format(exam))
        media = (media + exam) / 2
        if media > 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media))


if __name__ == '__main__':
    main()
