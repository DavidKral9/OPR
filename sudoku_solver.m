function sudoku_solver()
    % Example Sudoku puzzle (0 represents empty cells)
    board = [
        3, 0, 0, 8, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 0, 0, 0, 4, 0;
        4, 0, 1, 0, 0, 5, 0, 0, 7;
        0, 6, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 3, 0, 0, 0, 6, 0;
        0, 0, 0, 0, 6, 0, 2, 0, 0;
        0, 3, 0, 0, 0, 8, 0, 0, 0;
        0, 0, 8, 6, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0, 4
    ];

    disp('Original Sudoku puzzle:');
    print_board(board);

    if is_solvable(board)
        disp('The Sudoku puzzle is solvable. Solving...');
        solved_board = solve_sudoku(board);
        disp('Solved Sudoku puzzle:');
        print_board(solved_board);
    else
        disp('The Sudoku puzzle is not solvable.');
    end
end

function print_board(board)
    % Print the Sudoku board in a readable format.
    for i = 1:size(board, 1)
        if mod(i, 3) == 0 && i ~= 9
            disp('---------------------');
        end
        row = '';
        for j = 1:size(board, 2)
            if mod(j, 3) == 0 && j ~= 9
                row = strcat(row, sprintf('%d | ', board(i, j)));
            else
                row = strcat(row, sprintf('%d ', board(i, j)));
            end
        end
        disp(row);
    end
end

function valid = is_valid(board, num, row, col)
    % Check if a number can be placed at a specific position on the Sudoku board.
    % Parameters:
    % - board: Current Sudoku board (9x9 matrix).
    % - num: Number to be placed (1-9).
    % - row, col: Position on the board.

    % Check row
    if any(board(row, :) == num)
        valid = false;
        return;
    end

    % Check column
    if any(board(:, col) == num)
        valid = false;
        return;
    end

    % Check 3x3 block
    startRow = floor((row - 1) / 3) * 3 + 1;
    startCol = floor((col - 1) / 3) * 3 + 1;
    block = board(startRow:startRow+2, startCol:startCol+2);
    if any(block(:) == num)
        valid = false;
        return;
    end

    valid = true;
end

function board = solve_sudoku(board)
    % Recursively solve the Sudoku puzzle using the backtracking algorithm.
    % Returns the solved board.

    [row, col] = find(board == 0, 1); % Find the first empty cell
    if isempty(row)
        return; % The board is complete
    end

    for num = 1:9
        if is_valid(board, num, row, col)
            board(row, col) = num; % Place the number

            % Recursive call to solve the next cell
            solved_board = solve_sudoku(board);
            if all(solved_board(:) ~= 0)
                board = solved_board;
                return;
            end

            board(row, col) = 0; % Backtrack
        end
    end
end

function solvable = is_solvable(board)
    % Check if the given Sudoku board is solvable.
    % This is done by ensuring no row, column, or 3x3 block has duplicate numbers.

    for row = 1:9
        for col = 1:9
            num = board(row, col);
            if num ~= 0
                board(row, col) = 0; % Temporarily remove the number
                if ~is_valid(board, num, row, col)
                    solvable = false;
                    return;
                end
                board(row, col) = num; % Restore the number
            end
        end
    end

    % Try solving the board to ensure it has a solution
    try
        solved_board = solve_sudoku(board);
        solvable = all(solved_board(:) ~= 0);
    catch
        solvable = false;
    end
end
