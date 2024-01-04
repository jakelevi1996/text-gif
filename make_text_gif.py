import argparse
from jutility import plotting, util

def main(args):
    if args.input_filename is None:
        s = input("Enter string to animate, then press enter: ")
    else:
        with open(args.input_filename) as f:
            s = f.read()

    if args.by_letter:
        data_list = s
    else:
        data_list = s.split()

    gif = plotting.Gif()

    for i, word in enumerate(data_list):
        print(
            "\rMaking frame %i/%i..." % (i, len(data_list)),
            end="",
            flush=True,
        )

        gif.add_plot_frame(
            plotting.Text(
                0.5,
                0.5,
                word,
                size=args.font_size,
                center_align=True,
            ),
            axis_properties=plotting.AxisProperties(axis_off=True),
        )

    print("\nDone")

    gif.save(
        output_name=args.output_name,
        dir_name=args.output_dir,
        frame_duration_ms=args.frame_duration_ms,
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--by_letter",          action="store_true")
    parser.add_argument("--input_filename",     type=str, default=None)
    parser.add_argument("--frame_duration_ms",  type=int, default=500)
    parser.add_argument("--font_size",          type=int, default=None)
    parser.add_argument("--output_dir",         type=str, default=None)
    parser.add_argument("--output_name", type=str, default="text_gif_output")
    args = parser.parse_args()

    if args.font_size is None:
        args.font_size = 200 if args.by_letter else 60

    with util.Timer("main"):
        main(args)
