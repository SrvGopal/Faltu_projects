

    printf("Enter the total days ");
    scanf("%d",&days);

    year = days / 365;
    weeks = (days /7 )%52;
    days = days / 365;

    printf("It is %d Years: %d weeks: %d days",
    year,weeks,days);

}
