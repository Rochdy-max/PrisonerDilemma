##
## EPITECH PROJECT, 2022
## Makefile
## File description:
## compile binary
##

SRC	=	src/main.py

NAME	=	prisoner_dilemma

SRC_TESTS	=	tests/unit_tests.py

UNIT_TESTS	=	unit_tests

all:	$(NAME)

$(NAME):
	@ln -s $(SRC) $(NAME)
	@chmod +x $(NAME)

clean:
	@rm -f *~

fclean:	clean
	@rm -f $(NAME)

re:	fclean all

tests_run:	$(UNIT_TESTS)

$(UNIT_TESTS):
	@python3 -m unittest discover -v tests "*_tests.py"

clean_tests:
	@rm -f *~

fclean_tests:	clean_tests
	@rm -f $(UNIT_TESTS)

re_tests:	fclean_tests tests_run

fclean_all: fclean fclean_tests

.PHONY:	all clean fclean re	\
	tests_run clean_tests fclean_tests fclean_all re_tests	\
	client	recli
