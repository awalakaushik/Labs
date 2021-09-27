import { Component, OnInit } from '@angular/core';

import { Stack } from './../common/models/data-structures/stack';

@Component({
  selector: 'app-stack',
  templateUrl: './stack.component.html',
  styleUrls: ['./stack.component.scss']
})
export class StackComponent implements OnInit {

  stack: Stack<number>;
  stackSize: number = 0;
  pushElement: number | undefined;
  errorMessage: string | any = "";

  constructor() { 
    this.stack = new Stack<number>();
  }

  ngOnInit(): void {
  }

  onSetMaxStackSizeButtonClicked(event: Event, stackSize: number): void {
    this.stack.size = stackSize;

    const maxSizeInputElement = event.target as HTMLInputElement;
    maxSizeInputElement.value = "";
  }

  onPushButtonClicked(event: Event, pushElement: number | undefined): void {
    
    if (!pushElement) {
      return;
    }

    try {
      this.stack.push(pushElement);
    }
    catch(err) {
      this.errorMessage = err;
    }
  }

  onPopButtonClicked(event: Event): void {
    try {
      this.stack.pop();
    }
    catch(err) {
      this.errorMessage = err;
    }
  }
}
